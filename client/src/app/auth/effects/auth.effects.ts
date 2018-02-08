import { Injectable } from '@angular/core';
import { Effect, Actions } from '@ngrx/effects';

import { Action } from '@ngrx/store';
import { AuthService } from '../../core/services/auth.service';
import { AuthActions } from '../actions/auth.actions';
import { Observable } from 'rxjs/Observable';


@Injectable()
export class AuthenticationEffects {
  constructor(
    private actions$: Actions,
    private authService: AuthService,
    private authActions: AuthActions
  ) { }

  // tslint:disable-next-line:member-ordering
  @Effect()
    Authorized$: Observable<Action> = this.actions$
    .ofType(AuthActions.LOGIN_REQUEST)
    .map(() => this.authActions.loginSuccess());
}
