from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas, auth
from database import get_db

router = APIRouter(
    prefix="/api/orders",
    tags=["orders"]
)

@router.get("", response_model=List[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    orders = db.query(models.Order).filter(models.Order.user_id == current_user.id).all()
    return orders

@router.post("", response_model=schemas.OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    total_amount = 0
    order_items = []
    
    # Calculate total and verify products
    for item in order.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with id {item.product_id} not found")
            
        price = product.price
        total_amount += price * item.quantity
        order_items.append(
            models.OrderItem(
                product_id=product.id,
                quantity=item.quantity,
                price_at_time=price
            )
        )
        
    db_order = models.Order(
        user_id=current_user.id,
        total_amount=total_amount,
        items=order_items
    )
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this order")
    return order

@router.put("/{order_id}", response_model=schemas.OrderResponse)
def update_order_status(order_id: int, status_update: str, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    # In a real app, only admins should update status to shipped/delivered
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this order")
        
    order.status = status_update
    db.commit()
    db.refresh(order)
    return order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_order(order_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this order")
        
    order.status = "Cancelled"
    db.commit()
    return {"message": "Order cancelled successfully"}
