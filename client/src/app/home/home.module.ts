import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
import { RouterModule } from '@angular/router';
import { HomeRoutes } from './home.routes';
import { DocumentListComponent } from './document-list/document-list.component';
import { DocumentItemComponent } from './document-list/document-item/document-item.component';
import { DocumentActions } from '../document/reducers/document.actions';
import { EffectsModule } from '@ngrx/effects';
import { DocumentEffects } from '../document/reducers/document.effects';
import { StoreModule } from '@ngrx/store';

@NgModule({
  imports: [
    RouterModule.forChild(HomeRoutes),
    CommonModule
  ],
  providers: [
    DocumentActions,
  ],
  declarations: [HomeComponent, DocumentListComponent, DocumentItemComponent]
})
export class HomeModule { }
