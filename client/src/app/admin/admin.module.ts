import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserListComponent } from './user-list/user-list.component';
import { DocumentListComponent } from './document-list/document-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { RouterModule } from '@angular/router';
import { AdminRoutes } from './admin.routes';
import { NavbarComponent } from './navbar/navbar.component';
import { PlainUserRolePipe, UserRolePipe } from './user-list/user-list.pipe';
import { UserDetailsComponent } from './user-list/user-details/user-details.component';
import { SharedModule } from '../shared/shared.module';
import { UserEditComponent } from './user-list/user-edit/user-edit.component';
import { ReactiveFormsModule } from '@angular/forms';
import { DocumentModule } from '../document/document.module';

@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    ReactiveFormsModule,
    DocumentModule,
    RouterModule.forChild(AdminRoutes)
  ],
  providers: [
  ],
  declarations: [
    UserListComponent,
    DocumentListComponent,
    DashboardComponent,
    NavbarComponent,
    UserRolePipe,
    PlainUserRolePipe,
    UserDetailsComponent,
    UserEditComponent
  ]
})
export class AdminModule { }
