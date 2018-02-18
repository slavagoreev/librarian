import { RoleGuard } from '../auth/guards/role.guard';
import { UserListComponent } from './user-list/user-list.component';
import { DocumentListComponent } from './document-list/document-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UserDetailsComponent } from './user-list/user-details/user-details.component';
import { UserEditComponent } from './user-list/user-edit/user-edit.component';

export const AdminRoutes = [
  {
    path: 'admin',
    canActivate: [ RoleGuard ],
    data: {
      expectedRole: 2
    },
    children: [
      {
        path: '',
        component: DashboardComponent,
      },
      {
        path: 'user-list',
        component: UserListComponent
      },
      {
        path: 'user/:id',
        children: [
          {
            path: 'edit',
            component: UserEditComponent
          },
          {
            path: '',
            component: UserDetailsComponent,
          },
        ]
      },
      {
        path: 'document-list',
        component: DocumentListComponent
      },
      {
        path: 'order-list',
        component: UserListComponent
      },
      {
        path: 'tag-list',
        component: DocumentListComponent
      }
    ]
  },
];
