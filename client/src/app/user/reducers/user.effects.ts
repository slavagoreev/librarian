import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { Effect, Actions } from '@ngrx/effects';

import { Action } from '@ngrx/store';
import { UserActions } from "./user.actions";
import { UserService } from '../../core/services/user.service';

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
}
