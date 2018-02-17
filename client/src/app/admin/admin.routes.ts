import { RoleGuard } from '../auth/guards/role.guard';
import { UserListComponent } from './user-list/user-list.component';
import { DocumentListComponent } from './document-list/document-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';

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
        path: 'document-list',
        component: DocumentListComponent
      }
    ]
  },
];
