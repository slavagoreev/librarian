import { RouterModule, Routes } from '@angular/router';
// Todo auth guard
//import { CanActivateViaAuthGuard } from './core/guards/auth.guard';


export const routes: Routes = [
  { path: '', loadChildren: './home/home.module#HomeModule' },
  // Todo { path: '**', component: PageNotFoundComponent }
];
