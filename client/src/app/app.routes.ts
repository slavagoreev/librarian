import { RouterModule, Routes } from '@angular/router';
import { CanActivateViaAuthGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: '', loadChildren: './home/home.module#HomeModule',
    canActivate: [ CanActivateViaAuthGuard ],
  },
  {
    path: 'documents', loadChildren: './home/home.module#HomeModule',
    canActivate: [ CanActivateViaAuthGuard ]
  },
  {
    path: 'auth',
    loadChildren: './auth/auth.module#AuthModule'
  }
  // Todo { path: '**', component: PageNotFoundComponent }
];
