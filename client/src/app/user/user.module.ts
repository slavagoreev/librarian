import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { UserRoutes } from './user.routes';
import { AdminModule } from '../admin/admin.module';

@NgModule({
  imports: [
    CommonModule,
    AdminModule,
    RouterModule.forChild(UserRoutes),
  ],
  declarations: []
})
export class UserModule { }
