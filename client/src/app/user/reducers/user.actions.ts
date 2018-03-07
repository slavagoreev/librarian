import { Action } from '@ngrx/store';
import { Order } from '../../shared/models/orders.model';

export class UserActions {
  static GET_USER_ORDERS = 'GET_USER_ORDERS';
  static GET_USER_ORDERS_SUCCESS = 'GET_USER_ORDERS_SUCCESS';
  static ADD_NEW_ORDER = 'ADD_NEW_ORDER';
  static ADD_NEW_ORDER_SUCCESS = 'ADD_NEW_ORDER_SUCCESS';
  static CHANGE_ORDER_STATUS = 'CHANGE_ORDER_STATUS';
  static CHANGE_ORDER_STATUS_SUCCESS = 'CHANGE_ORDER_STATUS_SUCCESS';

  getUserOrders() {
    return { type: UserActions.GET_USER_ORDERS };
  }

  getUserOrdersSuccess(orders: Order[]) {
    return {
      type: UserActions.GET_USER_ORDERS_SUCCESS,
      payload: orders
    };
  }

  addNewOrder(document_id: number) {
    return {
      type: UserActions.ADD_NEW_ORDER,
      payload: document_id
    };
  }

  addNewOrderSuccess(order: Order) {
    return {
      type: UserActions.ADD_NEW_ORDER_SUCCESS,
      payload: order
    };
  }

  changeOrderStatus(status: number, order_id: number) {
    return {
      type: UserActions.CHANGE_ORDER_STATUS,
      payload: { status, order_id }
    };
  }

  changeOrderStatusSuccess(order: Order) {
    return {
      type: UserActions.CHANGE_ORDER_STATUS_SUCCESS,
      payload: order
    };
  }
}
