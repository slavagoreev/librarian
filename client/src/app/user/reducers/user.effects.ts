import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { Effect, Actions } from '@ngrx/effects';

import { Action } from '@ngrx/store';
import { UserActions } from "./user.actions";
import { UserService } from '../../core/services/user.service';
import { Order } from '../../shared/models/orders.model';

@Injectable()
export class UserEffects {
  constructor(
    private actions$: Actions,
    private userService: UserService,
    private userActions: UserActions
  ) { }

  @Effect()
  GetUserOrders$: Observable<Action> = this.actions$
    .ofType(UserActions.GET_USER_ORDERS)
    .switchMap(() => this.userService.getOrders())
    .filter((orders) => orders.length > 0)
    .map((orders) => this.userActions.getUserOrdersSuccess(orders));

  @Effect()
  AddNewOrder$ = this.actions$
    .ofType(UserActions.ADD_NEW_ORDER)
    .switchMap((action: any) => {
      return this.userService.bookTheDocument(action.payload);
    })
    .map((order: Order) => this.userActions.addNewOrderSuccess(order));

  /*@Effect()
  ChangeOrderStatus$ = this.actions$
    .ofType(UserActions.CHANGE_ORDER_STATUS)
    .switchMap((action: any) => {
      return this.userService.setStatusForOrder(action.payload.order_id, action.payload.status);
    })
    .map((order: Order) => this.userActions.addNewOrderSuccess(action.payload.status));*/
}
