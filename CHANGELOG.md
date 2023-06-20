#### 0.1.1 (2023-06-20)

##### Chores

*  update schemas according to newly nested models ([86660bfe](https://github.com/mihamieat/my-store/commit/86660bfeef9a5a25cb886b8de63f633553119350))
*  re-config pre-commits ([5ad7f18a](https://github.com/mihamieat/my-store/commit/5ad7f18a7358abd6cb28ff5b71e51df0002de5a6))
*  add python-dotenv in requirements ([3b90e807](https://github.com/mihamieat/my-store/commit/3b90e807fcd2308ac42d9717d6bbc51ced5c5867))
*  lint db file ([76bc72b0](https://github.com/mihamieat/my-store/commit/76bc72b0de4697310e23a11ce837799a8df20aa0))
*  add project package information ([058a43c9](https://github.com/mihamieat/my-store/commit/058a43c93ad696d8e8d8f9a72f1197919150a54f))
* **pre-commit:**  add pylint config file ([c966c2d7](https://github.com/mihamieat/my-store/commit/c966c2d736bc9d9cbfbe678a1a52e334992d0ab9))

##### Documentation Changes

* **readme:**  update documentation ([8c4367b9](https://github.com/mihamieat/my-store/commit/8c4367b97d0623c0ebc6dc46c05349cb65bf1b74))
*  add missing docstrings in fucntions ([d73758f4](https://github.com/mihamieat/my-store/commit/d73758f4094bb09c1bd3d6ac3a70f699abcdf74f))
*  add license file ([79258667](https://github.com/mihamieat/my-store/commit/792586674b106e3ad6369d8b6d4bd7980d9f5c34))

##### New Features

*  add token refreshing mechanism ([56512329](https://github.com/mihamieat/my-store/commit/5651232906ae0614706510795ac25346cf2a0aaf))
*  add logout endpoint ([baa015fb](https://github.com/mihamieat/my-store/commit/baa015fb4a9371e829c2c3d296ad275415fa5a31))
*  add login endpoint ([1d118e79](https://github.com/mihamieat/my-store/commit/1d118e79ddf895e0e4c3eb6fdb0860fc6c2adcc8))
*  add user endpoints ([430a7cc8](https://github.com/mihamieat/my-store/commit/430a7cc8decd5866a08cc13cba99c33d4ab11afe))
*  create tag endpoints ([b041b8e6](https://github.com/mihamieat/my-store/commit/b041b8e6b2148feeebcf1cf06fcc4a26cc054603))
*  delete nodels with relationships ([23b78fe2](https://github.com/mihamieat/my-store/commit/23b78fe2e276ab08d990cf37968616f7c726d515))
*  create SQLAlchemy models ([fca50875](https://github.com/mihamieat/my-store/commit/fca508753af45f387e9c8c47341ad3f77e9b4792))
*  decorate responses ([9d2db34b](https://github.com/mihamieat/my-store/commit/9d2db34b8b3b23756fc7e5d30a35325a9b1c5b4e))
*  add marshmallow schema ([c74cd298](https://github.com/mihamieat/my-store/commit/c74cd2989a86c90dac345b31ace51b167c315f61))
*  create item resource ([2125bf1e](https://github.com/mihamieat/my-store/commit/2125bf1e4af4831cd9b122a8dee480b5a8ba575b))
*  create store resource ([5fc8974c](https://github.com/mihamieat/my-store/commit/5fc8974c180777a8ec51a8e1ef9779d4bb4a1e95))
*  allow to update an item ([e93c1054](https://github.com/mihamieat/my-store/commit/e93c10542e7234261ad9c6557f169d4fca7b034e))
*  allow to delete a store ([cdc79a07](https://github.com/mihamieat/my-store/commit/cdc79a07841d760867826321c40569ad0a399655))
*  allow to delete an item ([370dd4c7](https://github.com/mihamieat/my-store/commit/370dd4c73858aff84f7127a5c0c4f3fd0c6e9b69))
* **authorization:**
  *  jwt claims and authorization ([7ee32628](https://github.com/mihamieat/my-store/commit/7ee326284ff388106a0ea2a430abd864ea34b7e5))
  *  protect items with jwt ([493df25c](https://github.com/mihamieat/my-store/commit/493df25c239f44e368a2931eee82ae14b6643042))
* **tags:**  create many-to-many relationships ([5c268b28](https://github.com/mihamieat/my-store/commit/5c268b286f98c210f4425ff4b0900c364e12176d))

##### Bug Fixes

*  correct schema bugs ([c6cb307d](https://github.com/mihamieat/my-store/commit/c6cb307d91a7f0c8fa866321e7e7d1ea0f811bf8))
*  correct table name method name ([739792a6](https://github.com/mihamieat/my-store/commit/739792a68fbec9777a719a87df2c917d1b73b1b7))
*  correct class calling statement ([9b310799](https://github.com/mihamieat/my-store/commit/9b3107991eb1d7f6db9b312651289329d9352d92))
*  correct id types in schmas ([aa3b7486](https://github.com/mihamieat/my-store/commit/aa3b748675ae2dd7881270832e895acbc7e51c14))

##### Refactors

*  update models with sqlalchemy ([f93c34e3](https://github.com/mihamieat/my-store/commit/f93c34e31430fe00c10ff294ae7a9728bc745a91))
*  create app factory pattern ([727c5549](https://github.com/mihamieat/my-store/commit/727c55493213abfc9780dd9c2398721b93362a86))
*  correct store creation ([7bafc732](https://github.com/mihamieat/my-store/commit/7bafc732230f6b3103afd3e8e21e5fe9edd4aecb))
*  reorder commands in dockerfile ([78cf23b4](https://github.com/mihamieat/my-store/commit/78cf23b41ac36f9320adb10f7ec0e7f762c53aac))
*  handle error on creating store ([14bfa7ad](https://github.com/mihamieat/my-store/commit/14bfa7ad1dcaf707e711372b16db66df02101868))
*  handle error on creating items ([a714a37c](https://github.com/mihamieat/my-store/commit/a714a37cae52500c9f7c786a62562606d2b564ed))
*  use smorest abort ([d59f1ae8](https://github.com/mihamieat/my-store/commit/d59f1ae84acf5d6fd487365f3c66d5026e18498d))
* **api:**  import blueprints and smorest configuration ([6ab220c0](https://github.com/mihamieat/my-store/commit/6ab220c0024dd7769ed64cb601bc9ce1850f34e5))

##### Code Style Changes

*  lint code according to pre-commit hooks ([e94ccdc9](https://github.com/mihamieat/my-store/commit/e94ccdc9e48f0c3fe3338499a83104967c4e0db0))
