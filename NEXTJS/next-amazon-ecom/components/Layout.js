import Head from 'next/head';
import Link from 'next/link';
import React from 'react';

export default function Layout({ title, children }) {
  return (
    <div>
      <Head>
        <title>{title ? title + '- Amazon' : 'Amazon'}</title>
        <meta name="description" content="Amazon Ecom Website." />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className=" flex  min-h-screen flex-col justify-between">
        <header>
          <nav className="flex h-12 justify-between shadow-md items-center px-4 ">
            <Link href="/">
              <a className="text-lg font-bold">Amazon</a>
            </Link>
            <div>
              <Link href="/cart">
                <a className="p-2">Cart</a>
              </Link>
              <Link href="/login">
                <a className="p-2">Login</a>
              </Link>
            </div>
          </nav>
        </header>

        <main>main</main>
        <footer>footer</footer>
      </div>
    </div>
  );
}
