import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ProductService } from './services/product.service';
import { Category } from './models/category.models';
import { Product } from './models/product.model';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('online-store');

  categories: Category[] = [];
  selectedCategoryId!: number;

  constructor(private productService: ProductService) {
    this.categories = this.productService.getCategories();


    if (this.categories.length > 0) {
      this.selectedCategoryId = this.categories[0].id;
    }
  }

  selectCategory(id: number): void {
    this.selectedCategoryId = id;
  }

  getProducts(categoryId: number): Product[] {
    return this.productService.getProductsByCategory(categoryId);
  }

  selectedImages: { [productId: number]: string } = {};

  getMainImage(product: Product): string {
    return this.selectedImages[product.id] || product.images[0];
  }

  selectImage(productId: number, image: string): void {
    this.selectedImages[productId] = image;
  }


  shareWhatsapp(product: Product) {
    const t = `Check out this product: ${product.link} `
    const shareUrl = `https://wa.me/?text=${encodeURIComponent(t)}`;
    window.open(shareUrl, '_blank');
  }

  shareTelegram(product: Product) {
    const url = encodeURIComponent(product.link);
    const text = encodeURIComponent(product.name);
    const shareUrl = `https://t.me/share/url?url=${url}&text=${text}`;
    window.open(shareUrl, '_blank');
  }
}
