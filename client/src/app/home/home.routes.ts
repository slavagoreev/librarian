import { HomeComponent } from './home.component';
import { CanActivateViaAuthGuard } from '../auth/guards/auth.guard';
import { DocumentDetailsComponent } from './document-details/document-details.component';

export const HomeRoutes = [
  {
    path: '',
    canActivate: [ CanActivateViaAuthGuard ],
    children: [
      {
        path: '',
        component: HomeComponent,
      },
      {
        path: ':id',
        component: DocumentDetailsComponent
      }
    ]
  },
];
