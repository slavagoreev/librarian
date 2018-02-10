import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from './services/auth.service';
import { HttpService } from './services/http.service';
import { DocumentService } from './services/document.service';
import { HttpModule, XHRBackend, RequestOptions, Http } from '@angular/http';
import { CanActivateViaAuthGuard } from './guards/auth.guard';
import { EffectsModule } from '@ngrx/effects';
import { AuthenticationEffects } from '../auth/effects/auth.effects';
import { DocumentEffects } from '../document/reducers/document.effects';

export function httpInterceptor(
  backend: XHRBackend,
  defaultOptions: RequestOptions,
) {
  return new HttpService(backend, defaultOptions);
}

@NgModule({
  imports: [
    CommonModule
  ],
  providers: [
    AuthService,
    HttpService,
    DocumentService,
    CanActivateViaAuthGuard,
    {
      provide: HttpService,
      useFactory: httpInterceptor,
      deps: [ XHRBackend, RequestOptions]
    },
  ],
  declarations: [
  ]
})
export class CoreModule { }
