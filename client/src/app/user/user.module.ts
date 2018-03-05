import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { UserRoutes } from './user.routes';
import { AdminModule } from '../admin/admin.module';
import { EffectsModule } from '@ngrx/effects';
import { UserEffects } from './reducers/user.effects';
import { UserActions } from './reducers/user.actions';

@NgModule({
  imports: [
    CommonModule,
    AdminModule,
    RouterModule.forChild(UserRoutes),
    EffectsModule.forFeature([UserEffects])
  ],
  declarations: [],
  providers: [
    UserActions,
  ]
})
export class UserModule { }
