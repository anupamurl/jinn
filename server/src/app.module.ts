import { Module } from '@nestjs/common';
import { ArticlesModule } from './articles/articles.module';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { EventsModule } from './events/events.module';
import { join } from 'path';
import { ServeStaticModule } from '@nestjs/serve-static';
@Module({
  imports: [AuthModule, UsersModule, ArticlesModule, EventsModule  ,
  
    ServeStaticModule.forRoot({
      rootPath: join(__dirname, '../', 'build'),   // <-- path to the static files
    }),
]
  ,
  controllers: [],
  providers: [],
})
export class AppModule {}
