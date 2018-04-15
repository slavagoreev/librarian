import { Injectable } from '@angular/core';
import {
  Router,
  CanActivate,
  ActivatedRouteSnapshot, RouterStateSnapshot
} from '@angular/router';
import { AuthService } from '../../core/services/auth.service';
import * as decode from 'jwt-decode';
import { Store } from '@ngrx/store';
import { AppState } from '../../interfaces';
import { getAuthStatus } from '../reducers/selectors';
import { Subscription } from 'rxjs/Subscription';


@Injectable()
export class RoleGuard implements CanActivate {
  private isAuthenticated: boolean;
  private subscription: Subscription;

  constructor(
    private store: Store<AppState>,
    private userSerice: AuthService,
    private router: Router
  ) {}
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    this.subscription = this.store
      .select(getAuthStatus)
      .subscribe(isAuthenticated => {
        this.isAuthenticated = isAuthenticated;
        const expectedRole = route.data.expectedRole;
        const token = this.userSerice.getToken();
        // console.warn (expectedRole, token, decode(token));
        if (!this.isAuthenticated || !token || decode(token).role < expectedRole) {
          this.router.navigate(
            ['/auth/login'],
            { queryParams: { returnUrl: state.url }}
          );
          return false;
        }
        return true;
      });

    return this.isAuthenticated;
  }
}
