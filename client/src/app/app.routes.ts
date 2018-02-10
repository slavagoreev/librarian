import { RouterModule, Routes } from '@angular/router';
import { CanActivateViaAuthGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: 'documents', loadChildren: './home/home.module#HomeModule',
    canActivate: [ CanActivateViaAuthGuard ]
  },
  {
    path: 'auth',
    loadChildren: './auth/auth.module#AuthModule'
  },
  {
    path: '',
    loadChildren: './home/home.module#HomeModule',
    canActivate: [ CanActivateViaAuthGuard ]
  },
  { path: '**', redirectTo: 'documents' }
];
