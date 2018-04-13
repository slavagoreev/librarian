import { RoleGuard } from '../auth/guards/role.guard';
import { UserListComponent } from './user-list/user-list.component';
import { DocumentListComponent } from './document-list/document-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UserDetailsComponent } from './user-list/user-details/user-details.component';
import { UserEditComponent } from './user-list/user-edit/user-edit.component';
import { OrderListComponent } from "./order-list/order-list.component";
import {AddComponent} from './document-list/add/add.component';

export const AdminRoutes = [
  {
    path: 'librarian',
    canActivate: [ RoleGuard ],
    data: {
      expectedRole: 330,
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
        children: [
          {
            path: 'add',
            component: AddComponent,
          },
          {
            path: '',
            component: DocumentListComponent
          }
        ]
      },
      {
        path: 'order-list',
        component: OrderListComponent
      },
      {
        path: 'tag-list',
        component: DocumentListComponent
      }
    ]
  },
];
