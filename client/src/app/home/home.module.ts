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
import { GenreNavComponent } from './genre-nav/genre-nav.component';
import { LoaderComponent } from '../shared/components/loader/loader.component';
import { SharedModule } from '../shared/shared.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DocumentDetailsComponent } from './document-details/document-details.component';
import { DocumentInfoComponent } from './document-details/document-info/document-info.component';
import { DocumentModule } from '../document/document.module';

@NgModule({
  imports: [
    RouterModule.forChild(HomeRoutes),
    CommonModule,
    SharedModule,
    DocumentModule,
    NgbModule
  ],
  providers: [
    DocumentActions,
  ],
  declarations: [
    HomeComponent,
    DocumentListComponent,
    DocumentItemComponent,
    GenreNavComponent,
    DocumentDetailsComponent,
    DocumentInfoComponent
  ]
})
export class HomeModule { }
