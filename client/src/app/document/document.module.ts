import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EffectsModule } from '@ngrx/effects';
import { DocumentEffects } from './reducers/document.effects';
import { DocumentActions } from './reducers/document.actions';
import { DocumentTypePipe } from './document.pipe';
import { DocumentTypeClassPipe } from './document.pipe';
import { InfiniteScrollerDirective } from "./directives/infinite-scroller.directive";

@NgModule({
  imports: [
    CommonModule,
    EffectsModule.forFeature([DocumentEffects])
  ],
  exports: [
    DocumentTypePipe,
    DocumentTypeClassPipe,
    InfiniteScrollerDirective
  ],
  declarations: [
    DocumentTypePipe,
    DocumentTypeClassPipe,
    InfiniteScrollerDirective
  ],
  providers: [
    DocumentActions
  ]
})
export class DocumentModule { }
