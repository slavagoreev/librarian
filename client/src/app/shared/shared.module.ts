import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoaderComponent } from './components/loader/loader.component';
import { WINDOW_PROVIDERS } from './services/scroll.service';
import { NotFoundComponent } from './components/not-found/not-found.component';

@NgModule({
  imports: [
    CommonModule
  ],
  exports: [
    CommonModule,
    LoaderComponent,
    NotFoundComponent
  ],
  providers: [WINDOW_PROVIDERS],
  declarations: [LoaderComponent, NotFoundComponent]
})
export class SharedModule { }
