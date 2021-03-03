import { TestBed, async } from '@angular/core/testing';
import { AppComponent } from './app.component';

import { FileUploadComponent } from './file-upload.component'

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        AppComponent
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });
  
  it('should create file-upload component', () => {
    let component: FileUploadComponent;
    expect(component).toBeDefined();
  })
});
