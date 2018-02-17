import { HomeComponent } from './home.component';
import { CanActivateViaAuthGuard } from '../auth/guards/auth.guard';

export const HomeRoutes = [
  {
    path: '',
    canActivate: [ CanActivateViaAuthGuard ],
    component: HomeComponent,
    children: [
      {
        path: ':id',
        component: HomeComponent
      }
    ]
  },
];
