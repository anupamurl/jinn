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
    openai(req: any): Promise<void>;
    getUser(postSearch: any): Promise<void>;
    getkeyword(keyword: any, people: any): Promise<void>;
    searchData(req: any): Promise<string>;
}
