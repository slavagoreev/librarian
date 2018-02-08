import { Subscription } from 'rxjs/Subscription';
import { Observable } from 'rxjs/Observable';
import { Injectable, OnDestroy } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Store } from '@ngrx/store';
import { AppState } from '../../interfaces';
import { getAuthStatus } from '../../auth/reducers/selectors';


@Injectable()
export class CanActivateViaAuthGuard implements CanActivate, OnDestroy{
  isAuthenticated: boolean;
  subscription: Subscription;

  constructor(
    private store: Store<AppState>,
    private router: Router
  ) {
    console.warn(123)
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    console.warn('AuthGuard#canActivate called');
    this.subscription = this.store
      .select(getAuthStatus)
      .subscribe(isAuthenticated => {
        console.log (isAuthenticated)
        this.isAuthenticated = isAuthenticated;
        if (!isAuthenticated) {
          this.router.navigate(
            ['/auth/login'],
            { queryParams: { returnUrl: state.url }}
          );
        }
      });

    return this.isAuthenticated;
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
