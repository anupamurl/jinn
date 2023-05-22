
import { Controller, Get, HttpService, Post, Req, UseGuards } from '@nestjs/common';
import { JwtAuthGuard } from 'src/auth/guards/jwt-auth.guard';
import { ArticlesService } from './articles.service';
import {EventsGateway} from '../events/events.gateway'
import { WebSocketServer } from '@nestjs/websockets';
import { Server } from 'socket.io';

 

const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: `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`,
});
const openai = new OpenAIApi(configuration);


  
  // 


@Controller('article')
export class ArticlesController {
  constructor(private articlesService: ArticlesService , private EventsGateway : EventsGateway ,
    private readonly httpService: HttpService
    ) {}
    @WebSocketServer()
    public server: Server 
  @Get('all')
  getAllArticles() {
    console.log(`[ArticlesController] getAllArticles`)
    return this.articlesService.findAll();
  }

  @UseGuards(JwtAuthGuard)
  @Get('my')
  getMyArticles(@Req() req) {
    console.log(`[ArticlesController] getMyArticles`, req.user.email)
    return this.articlesService.findByOwnerEmail(req.user.email);
  }



 
  @Post('getopenai')
async  openai(@Req() req) {



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
} catch (error) {
  if (error.response) {
    console.log(error.response.status);
    console.log(error.response.data);
  } else {
    console.log(error.message);
  }
}
  }



  async getUser(postSearch){
    console.log("getUser called")
    await this.httpService.get('http://127.0.0.1:8001/mainbox?keyword='+postSearch ).toPromise();   
  }
  
  
 async getkeyword(keyword,people){
    console.log("getkeyword called")
    await this.httpService.get('http://127.0.0.1:8001?keyword='+keyword+'&people='+people).toPromise();  
  }
  
  @UseGuards(JwtAuthGuard)
  @Post('search')
  async searchData(@Req() req) {
   console.log(`[ArticlesController] getMyArticles`, req.body) 
   
   this.getUser(req.body.postSearch) 
 
   this.getkeyword(req.body.keyword,req.body.people)  
   

   return "data" ;
   
  }


 

}
