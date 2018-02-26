import { UserState, InitialUserState } from './user.state';
import { UserActions } from './user.actions';

export const initialState: UserState = new InitialUserState() as UserState;

export function reducer(state = initialState, { type, payload }: any): UserState {
  switch (type) {
    case UserActions.GET_USER_ORDERS_SUCCESS:
      return state.merge({ orders: payload }) as UserState;

    default:
      return state;
  }
};
