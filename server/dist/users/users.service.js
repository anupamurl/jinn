"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UsersService = void 0;
const common_1 = require("@nestjs/common");
let UsersService = class UsersService {
    constructor() {
        this.users = [
            {
                email: 'israel.lavi@gmail.com',
                name: 'Israel Lavi',
                password: '123456'
            },
            {
                email: 'john.smith@gmail.com',
                name: 'John Smith',
                password: '123456'
            },
        ];
    }
    async findOne(email) {
        return this.users.find(user => user.email === email);
    }
    async validateUser(email, password) {
        console.log(`[UsersService] validateUser, email: ${email}, password: ${password}`);
        const user = this.users.find(user => user.email === email && user.password === password);
        if (user) {
            console.log('[UsersService] validateUser: found user', user);
            return Object.assign(Object.assign({}, user), { password: undefined });
        }
        return undefined;
    }
};
UsersService = __decorate([
    (0, common_1.Injectable)()
], UsersService);
exports.UsersService = UsersService;
//# sourceMappingURL=users.service.js.map