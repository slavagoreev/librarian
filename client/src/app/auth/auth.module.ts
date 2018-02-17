import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { LoginComponent } from './components/login/login.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';

import { AuthRoutes as routes } from './auth.routes';
import { SharedModule } from '../shared/shared.module';
import { ReactiveFormsModule } from '@angular/forms';
import { AuthActions } from './actions/auth.actions';
import { AuthenticationEffects } from './effects/auth.effects';
import { EffectsModule } from '@ngrx/effects';
import { CanActivateViaAuthGuard } from './guards/auth.guard';
import { JwtHelperService, JwtModule } from '@auth0/angular-jwt';
import { RoleGuard } from './guards/role.guard';

@NgModule({
  providers: [
    AuthActions,
    CanActivateViaAuthGuard,
    RoleGuard
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    EffectsModule.forFeature([
      AuthenticationEffects
    ]),
    SharedModule,
    ReactiveFormsModule
  ],
  declarations: [
    LoginComponent,
    SignUpComponent
  ]
})
export class AuthModule { }
