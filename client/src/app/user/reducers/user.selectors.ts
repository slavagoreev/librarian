import { AppState } from './../../interfaces';
import { createSelector } from 'reselect';
import { UserState } from './user.state';
import { Order } from '../../shared/models/orders.model';

function getUserState(state: AppState): UserState {
  return state.user;
}

const fetchUserOrders = function(state: UserState): Order[] {
  return state.orders.toJS();
};

// *************************** PUBLIC API's ****************************
export const getUserOrders = createSelector(getUserState, fetchUserOrders);
