import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { StoreModule } from '@ngrx/store';
import { RouterModule, PreloadAllModules } from '@angular/router';
import { AppComponent } from './app.component';
import { EffectsModule } from '@ngrx/effects';

import { routes } from './app.routes';
import { environment } from './../environments/environment.prod';

// Modules
import { SharedModule } from './shared/shared.module';
import { CoreModule } from './core/core.module';
import { HomeModule } from './home/home.module';
import { LayoutModule } from './layout/layout.module';
import { DocumentModule } from './document/document.module';
import { reducers, metaReducers } from './app.reducers';


import 'rxjs/add/operator/map';
import 'rxjs/add/operator/filter';
import 'rxjs/add/operator/switchMap';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/finally';
import 'rxjs/add/observable/of';
import { DocumentEffects } from './document/reducers/document.effects';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    StoreModule.forRoot(reducers, { metaReducers }),
    //!environment.production ? StoreDevtoolsModule.instrument() : [],

    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules }),
    EffectsModule.forRoot([DocumentEffects]),
    BrowserModule,
    FormsModule,
    HttpModule,
    HomeModule,
    LayoutModule,
    DocumentModule,
    CoreModule,
    SharedModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
