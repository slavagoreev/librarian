import { Map, Record, List } from 'immutable';
import { Order } from '../../shared/models/orders.model';

export interface UserState extends Map<string, any> {
  orders: List<Order>;
}

export const InitialUserState = Record({
  orders: List()
});
