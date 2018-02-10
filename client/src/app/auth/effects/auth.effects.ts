import { Injectable } from '@angular/core';
import { Effect, Actions } from '@ngrx/effects';

import { Action, Store } from '@ngrx/store';
import { AuthService } from '../../core/services/auth.service';
import { AuthActions } from '../actions/auth.actions';
import { Observable } from 'rxjs/Observable';
import { AppState } from '../../interfaces';



@Injectable()
export class AuthenticationEffects {
  constructor(
    private actions$: Actions,
    private authService: AuthService,
    private store$: Store<AppState>,
    private authActions: AuthActions
  ) { }

  // tslint:disable-next-line:member-ordering
  @Effect()
  Authorized$: Observable<Action> = this.actions$
    .ofType(AuthActions.AUTHORIZE)
    .withLatestFrom(this.store$)
    .filter(() => this.authService.isLoggedIn())
    .map(() => this.authActions.loginSuccess({
      user: this.authService.getUserData(),
      token: this.authService.getToken()
    }));
}
