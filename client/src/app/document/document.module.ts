import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EffectsModule } from '@ngrx/effects';
import { DocumentEffects } from './reducers/document.effects';
import { DocumentActions } from './reducers/document.actions';

@NgModule({
  imports: [
    CommonModule,
    EffectsModule.forFeature([DocumentEffects])
  ],
  declarations: [],
  providers: [
    DocumentActions
  ]
})
export class DocumentModule { }
