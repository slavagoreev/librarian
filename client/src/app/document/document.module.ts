import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EffectsModule } from '@ngrx/effects';
import { DocumentEffects } from './reducers/document.effects';

@NgModule({
  imports: [
    CommonModule,
    EffectsModule.forFeature([DocumentEffects])
  ],
  declarations: [],
  providers: [
  ]
})
export class DocumentModule { }
