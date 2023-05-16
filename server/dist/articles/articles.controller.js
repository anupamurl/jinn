"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ArticlesController = void 0;
const common_1 = require("@nestjs/common");
const jwt_auth_guard_1 = require("../auth/guards/jwt-auth.guard");
const articles_service_1 = require("./articles.service");
const events_gateway_1 = require("../events/events.gateway");
const websockets_1 = require("@nestjs/websockets");
const socket_io_1 = require("socket.io");
const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    apiKey: `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`,
});
const openai = new OpenAIApi(configuration);
let ArticlesController = class ArticlesController {
    constructor(articlesService, EventsGateway, httpService) {
        this.articlesService = articlesService;
        this.EventsGateway = EventsGateway;
        this.httpService = httpService;
    }
    getAllArticles() {
        console.log(`[ArticlesController] getAllArticles`);
        return this.articlesService.findAll();
    }
    getMyArticles(req) {
        console.log(`[ArticlesController] getMyArticles`, req.user.email);
        return this.articlesService.findByOwnerEmail(req.user.email);
    }
    async openai(req) {
        try {
            const response = await openai.createCompletion({
                model: "text-davinci-003",
                prompt: `Read this article: https://peping.in/blog/home-remedies-for-indigestion-the-ultimate-guide/
Write summery as human
Write Key points.
Find top SEO keywords
Find 10  Keyword Density`,
                temperature: 0.7,
                max_tokens: 256,
                top_p: 1,
                frequency_penalty: 0,
                presence_penalty: 0,
            });
            console.log(response.data.choices[0].text);
        }
        catch (error) {
            if (error.response) {
                console.log(error.response.status);
                console.log(error.response.data);
            }
            else {
                console.log(error.message);
            }
        }
    }
    searchData(req) {
        console.log(`[ArticlesController] getMyArticles`, req.body);
        return this.httpService.get('http://127.0.0.1:8001?keyword=' + req.body.keyword);
        return "data";
    }
};
__decorate([
    (0, websockets_1.WebSocketServer)(),
    __metadata("design:type", socket_io_1.Server)
], ArticlesController.prototype, "server", void 0);
__decorate([
    (0, common_1.Get)('all'),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", []),
    __metadata("design:returntype", void 0)
], ArticlesController.prototype, "getAllArticles", null);
__decorate([
    (0, common_1.UseGuards)(jwt_auth_guard_1.JwtAuthGuard),
    (0, common_1.Get)('my'),
    __param(0, (0, common_1.Req)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", void 0)
], ArticlesController.prototype, "getMyArticles", null);
__decorate([
    (0, common_1.Post)('getopenai'),
    __param(0, (0, common_1.Req)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], ArticlesController.prototype, "openai", null);
__decorate([
    (0, common_1.UseGuards)(jwt_auth_guard_1.JwtAuthGuard),
    (0, common_1.Post)('search'),
    __param(0, (0, common_1.Req)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", void 0)
], ArticlesController.prototype, "searchData", null);
ArticlesController = __decorate([
    (0, common_1.Controller)('article'),
    __metadata("design:paramtypes", [articles_service_1.ArticlesService, events_gateway_1.EventsGateway,
        common_1.HttpService])
], ArticlesController);
exports.ArticlesController = ArticlesController;
//# sourceMappingURL=articles.controller.js.map