import { Module } from '@nestjs/common';
import { ArticlesModule } from './articles/articles.module';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { EventsModule } from './events/events.module';
@Module({
  imports: [AuthModule, UsersModule, ArticlesModule, EventsModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
