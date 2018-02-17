import { RouterModule, Routes } from '@angular/router';
import { CanActivateViaAuthGuard } from './auth/guards/auth.guard';
import { NotFoundComponent } from './shared/components/not-found/not-found.component';

export const routes: Routes = [
  {
    path: 'documents',
    loadChildren: './home/home.module#HomeModule'
  },
  {
    path: 'auth',
    loadChildren: './auth/auth.module#AuthModule'
  },
  {
    path: '',
    pathMatch: 'full', redirectTo: 'documents'
  },
  { path: '**', component: NotFoundComponent }
];
