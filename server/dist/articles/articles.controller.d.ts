import { HttpService } from '@nestjs/common';
import { ArticlesService } from './articles.service';
import { EventsGateway } from '../events/events.gateway';
import { Server } from 'socket.io';
export declare class ArticlesController {
    private articlesService;
    private EventsGateway;
    private readonly httpService;
    constructor(articlesService: ArticlesService, EventsGateway: EventsGateway, httpService: HttpService);
    server: Server;
    getAllArticles(): Promise<import("./articles.interface").IArticle[]>;
    getMyArticles(req: any): Promise<import("./articles.interface").IArticle[]>;
    searchData(req: any): import("rxjs").Observable<import("axios").AxiosResponse<any>> | "data";
}
