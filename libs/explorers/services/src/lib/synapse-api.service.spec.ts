/* eslint-disable no-template-curly-in-string */
// -------------------------------------------------------------------------- //
// External
// -------------------------------------------------------------------------- //
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

// -------------------------------------------------------------------------- //
// Internal
// -------------------------------------------------------------------------- //
import { provideHttpClient } from '@angular/common/http';
import { synapseWikiMock } from '@sagebionetworks/explorers/testing';
import { SynapseApiService } from './synapse-api.service';

// -------------------------------------------------------------------------- //
// Tests
// -------------------------------------------------------------------------- //
describe('Service: Synapse API', () => {
  let synapseApiService: SynapseApiService;
  let httpMock: HttpTestingController;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting(), SynapseApiService],
    });

    synapseApiService = TestBed.inject(SynapseApiService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should create', () => {
    expect(synapseApiService).toBeDefined();
  });

  it('should get data from Synapse API', () => {
    synapseApiService.getWikiMarkdown('syn25913473', synapseWikiMock.id).subscribe((response) => {
      expect(response).toEqual(synapseWikiMock);
    });

    const req = httpMock.expectOne(
      'https://repo-prod.prod.sagebase.org/repo/v1/entity/syn25913473/wiki/' + synapseWikiMock.id,
    );
    expect(req.request.method).toBe('GET');
    req.flush(synapseWikiMock);
  });

  it('should replace links', () => {
    const res = synapseApiService.renderHtml('[test](https://test.com)');
    expect(res).toEqual('<a href="https://test.com" target="_blank">test</a>');
  });

  it('should replace synapse links', () => {
    const res = synapseApiService.renderHtml('[test](syn123)');
    expect(res).toEqual('<a href="https://synapse.org/#!Synapse:syn123" target="_blank">test</a>');
  });

  it('should replace bold', () => {
    const res = synapseApiService.renderHtml('**test**');
    expect(res).toEqual('<b>test</b>');
  });

  it('should replace email', () => {
    const res = synapseApiService.renderHtml('agora@sagebionetworks.org');
    expect(res).toEqual(
      '<a class="link email-link" href="mailto:agora@sagebionetworks.org">agora@sagebionetworks.org</a>',
    );
  });

  it('should replace image', () => {
    const res = synapseApiService.renderHtml('${?fileName=test.png}');
    expect(res).toEqual('<img src="test.png" alt="" />');
  });

  it('should replace video', () => {
    const res = synapseApiService.renderHtml('${?vimeoId=123}');
    expect(res).toEqual(
      '<iframe src="https://player.vimeo.com/video/123?autoplay=0&speed=1" frameborder="0" allow="autoplay; encrypted-media" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>',
    );
  });
});
