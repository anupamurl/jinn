import { HttpModule, Module } from '@nestjs/common';
import { ArticlesController } from './articles.controller';
import { ArticlesService } from './articles.service';
import { EventsModule } from 'src/events/events.module';

@Module({
  imports : [EventsModule , HttpModule ],
  controllers: [ArticlesController  ],
  providers: [ArticlesService    ],
  exports: [ArticlesService],
 
})
export class ArticlesModule {}
