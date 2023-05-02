import { IUser } from './users.interface';
export declare class UsersService {
    private readonly users;
    findOne(email: string): Promise<IUser | undefined>;
    validateUser(email: string, password: string): Promise<IUser | undefined>;
}
