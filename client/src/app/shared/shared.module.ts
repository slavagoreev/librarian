import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoaderComponent } from './loader/loader.component';
import { WINDOW_PROVIDERS } from './services/scroll.service';

@NgModule({
  imports: [
    CommonModule
  ],
  exports: [
    CommonModule,
    LoaderComponent
  ],
  providers: [WINDOW_PROVIDERS],
  declarations: [LoaderComponent]
})
export class SharedModule { }
