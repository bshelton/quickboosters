import React, { Component, lazy, Suspense } from 'react';
import Swiper from "react-id-swiper";

const params = {
  pagination: ".swiper-pagination",
  paginationClickable: true,
  nextButton: ".swiper-button-next",
  prevButton: ".swiper-button-prev",
  autoplay: true,
  pagination: {
    el: ".swiper-pagination",
    type: "bullets",
  },
  scrollbar: {
    el: ".swiper-scrollbar",
    draggable: true,
  },
};

function Home() {
  return (
    <div>
      <Swiper {...params}>
        <div style={{ backgroundImage: "url(/bg-default.jpg)" }}>
          <div className="v-center center">
            <h1 className="display">The safest boost your account</h1>
            <h2>Safe and reliable elo boosting and coaching services</h2>
            <button className="btn">Signup now</button>
          </div>
        </div>
        <div style={{ backgroundImage: "url(/bg.jpg)" }}>
          <div className="v-center center">
            <h1 className="display">The safest LoL boost experience</h1>
            <h2>Safe and reliable elo boosting and coaching services</h2>
            <button className="btn ">Signup now</button>
          </div>
        </div>
      </Swiper>
      <div className="bp-block">
        <div className="wrapper center">
          <h3>
            Why our Elo boost is different and how we keep your account safe
          </h3>
        </div>
        <div className="wrapper-m">
          <div className="center">
            We're an experienced boosting organisation with over 400 orders
            completed and without a single ban for account sharing. We pick each
            booster with great care to guarantee a professional service.
          </div>
        </div>
      </div>
      <div class="bp-cards wrapper">
        <ul className="grid--auto-c">
          <li>
            <img src="/2.png" />

            <div className="content">
              <a href="{{post.link}}">
                <h3>Lorem ipsum dolor sit</h3>
              </a>
              <div className="excerpt">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud
              </div>
              <a className="read-more" href="#">
                Read more
              </a>
            </div>
          </li>
          <li>
            <img src="/1.png" />
            <div className="content">
              <a href="{{post.link}}">
                <h3>Lorem ipsum dolor sit</h3>
              </a>
              <div className="excerpt">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud
              </div>
              <a className="read-more" href="#">
                Read more
              </a>
            </div>
          </li>
          <li>
            <img src="3.png" />
            <div className="content">
              <a href="{{post.link}}">
                <h3>Lorem ipsum dolor sit</h3>
              </a>
              <div className="excerpt">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud
              </div>
              <a className="read-more" href="#">
                Read more
              </a>
            </div>
          </li>
        </ul>
      </div>

      <section class="bp-block bp-text-image   alignfull ">
        <div class="wrapper">
          <div class="grid--2">
            <div
              class="itb-image lazyloaded"
              data-bg="https://images.unsplash.com/photo-1519669556878-63bdad8a1a49?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1502&q=80"
              style={{
                backgroundImage:
                  "url(https://images.unsplash.com/photo-1519669556878-63bdad8a1a49?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1502&q=80)",
              }}
            >
              <div className="overlay-move"></div>
            </div>
            <div class="itb-text">
              <h2 data-aos="fade-up" class="aos-init aos-animate">
                Lorem ipsum dolor{" "}
              </h2>
              <div
                data-aos="fade-up"
                data-aos-delay="100"
                class="aos-init aos-animate"
              >
                <p>
                  Duis aute irure dolor in reprehenderit in voluptate velit esse
                  cillum dolore eu fugiat nulla pariatur. Excepteur sint
                  occaecat cupidatat non
                </p>
              </div>
              <div
                class="itb-footer aos-init aos-animate"
                data-aos="fade-up"
                data-aos-delay="200"
              >
                <ul>
                  <li>
                    <a href="http://blockpress.loc/" class="btn btn--sec">
                      Officia deserunt
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="bp-block bp-text-image   alignfull ">
        <div class="wrapper">
          <div class="grid--2  image-on-left">
            <div
              class="itb-image lazyloaded"
              style={{
                backgroundImage:
                  "url(https://images.unsplash.com/photo-1581351123004-757df051db8e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80)",
              }}
            >
              <div className="overlay-move"></div>
            </div>
            <div class="itb-text">
              <h2 data-aos="fade-up" class="aos-init aos-animate">
                Lorem ipsum dolor{" "}
              </h2>
              <div
                data-aos="fade-up"
                data-aos-delay="100"
                class="aos-init aos-animate"
              >
                <p>
                  Duis aute irure dolor in reprehenderit in voluptate velit esse
                  cillum dolore eu fugiat nulla pariatur. Excepteur sint
                  occaecat cupidatat non
                </p>
              </div>
              <div
                class="itb-footer aos-init aos-animate"
                data-aos="fade-up"
                data-aos-delay="200"
              >
                <ul>
                  <li>
                    <a href="http://blockpress.loc/" class="btn btn--ghost">
                      Officia deserunt
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

    </div>
  );
}
export default Home;
