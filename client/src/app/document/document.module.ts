import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EffectsModule } from '@ngrx/effects';
import { DocumentEffects } from './reducers/document.effects';
import { DocumentActions } from './reducers/document.actions';
import { DocumentTypePipe } from './document.pipe';
import { DocumentTypeClassPipe } from './document.pipe';

@NgModule({
  imports: [
    CommonModule,
    EffectsModule.forFeature([DocumentEffects])
  ],
  exports: [
    DocumentTypePipe,
    DocumentTypeClassPipe
  ],
  declarations: [
    DocumentTypePipe,
    DocumentTypeClassPipe
  ],
  providers: [
    DocumentActions,
  ]
})
export class DocumentModule { }
