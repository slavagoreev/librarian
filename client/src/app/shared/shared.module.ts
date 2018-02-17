import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoaderComponent } from './components/loader/loader.component';
import { WINDOW_PROVIDERS } from './services/scroll.service';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { NotificationComponent } from './components/notification/notification.component';
import { ReversePipe } from './pipes/reverse.pipe';
import { NotificationService } from './components/notification/notification.service';

@NgModule({
  imports: [
    CommonModule,
  ],
  exports: [
    CommonModule,
    LoaderComponent,
    NotificationComponent,
    NotFoundComponent,
  ],
  providers: [
    WINDOW_PROVIDERS,
    NotificationService
  ],
  declarations: [
    LoaderComponent,
    NotFoundComponent,
    NotificationComponent,
    ReversePipe
  ]
})
export class SharedModule { }
