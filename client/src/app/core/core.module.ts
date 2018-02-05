import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from './services/auth.service';
import { HttpService } from './services/http.service';
import { DocumentService } from './services/document.service';
import { HttpModule, XHRBackend, RequestOptions, Http } from '@angular/http';

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
    {
      provide: HttpService,
      useFactory: httpInterceptor,
      deps: [ XHRBackend, RequestOptions]
    },
  ],
  declarations: []
})
export class CoreModule { }
