import { ArticlesService } from './articles.service';
export declare class ArticlesController {
    private articlesService;
    constructor(articlesService: ArticlesService);
    getAllArticles(): Promise<import("./articles.interface").IArticle[]>;
    getMyArticles(req: any): Promise<import("./articles.interface").IArticle[]>;
}
