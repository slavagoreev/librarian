import { UserState, InitialUserState } from './user.state';
import { UserActions } from './user.actions';
import { Order } from '../../shared/models/orders.model';

export const initialState: UserState = new InitialUserState() as UserState;

export function reducer(state = initialState, { type, payload }: any): UserState {
  let order, orders;
  switch (type) {
    case UserActions.GET_USER_ORDERS_SUCCESS:
      return state.merge({ orders: payload }) as UserState;

    case UserActions.ADD_NEW_ORDER_SUCCESS:
      order = payload;

      // return the same state if the item is already included.
      if (state.orders.find(o => o.order_id == order.order_id)) {
        return state;
      }
      orders = state.orders.push(order);

      return state.merge({
        orders: orders
      }) as UserState;

    /*case UserActions.CHANGE_ORDER_STATUS_SUCCESS:
      orderId = payload;
      state.orders.forEach((o, index) => {
        if (o.order_id === payload.id) {
          state.orders.set(index, order);
        }
      });
      return state.merge({
        orders: orders
      }) as UserState;
*/
    default:
      return state;
  }
};
