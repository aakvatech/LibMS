<template>
    <v-app>
        <v-app-bar>
            <PdfTitlebar :title="book.book_title" @close-reader="closeReader" @toggle-toc="toggleToc" />
        </v-app-bar>
        <v-main>
            <v-row>
                <PdfToc :toc="toc" :isTocVisible="isTocVisible" @render-page="navigateToPage" />

                <v-col class="d-flex justify-start align-items-center">
                    <v-btn icon @click="previousPage">
                        <v-icon>mdi-chevron-left</v-icon>
                        <v-tooltip activator="parent" location="top">Previous Page</v-tooltip>
                    </v-btn>
                </v-col>
                <v-col class="justify-center align-items-center">
                    <div class="pdf-container">
                        <v-card class="mt-0" hover>
                            <canvas id="pdf-canvas"> </canvas>
                        </v-card>
                    </div>
                </v-col>
                <v-col class="d-flex justify-end align-items-center">
                    <v-btn icon @click="nextPage">
                        <v-icon>mdi-chevron-right</v-icon>
                        <v-tooltip activator="parent" location="top">Next Page</v-tooltip>
                    </v-btn>
                </v-col>

                <v-snackbar v-model="showSnackbar" :color="snackbarColor" timeout="1000" rounded>
                    {{ snackbarText }}
                    <v-btn small color="white" text @click="showSnackbar = false">Close</v-btn>
                </v-snackbar>
            </v-row>
        </v-main>
        <v-bottom-navigation class="bg-light">
            <v-spacer></v-spacer>
            <div class="d-flex justify-content-center align-items-center">
                <v-btn icon @click="previousPage">
                    <v-icon>mdi-arrow-left</v-icon>
                    <v-tooltip activator="parent" location="top">Previous Page</v-tooltip>
                </v-btn>
                <v-text-field v-model="manualPage" @keyup.enter="navigateToPage(manualPage)"
                    @mouseleave="updatePlaceholder" class="mx-2 page-input-field" min="1" :max="totalPages" outlined
                    style="width: 200px;">
                </v-text-field>
                <v-btn icon @click="nextPage">
                    <v-icon>mdi-arrow-right</v-icon>
                    <v-tooltip activator="parent" location="top">Next Page</v-tooltip>
                </v-btn>
            </div>
            <v-spacer></v-spacer>
            <div class="d-flex justify-end align-items-right">
                <v-btn icon size="small" @click="zoomOut" class="mb-2">
                    <v-icon>mdi-minus</v-icon>
                    <v-tooltip activator="parent" location="top">zoomOut</v-tooltip>
                </v-btn>
                <v-btn icon size="small" @click="zoomIn" class="mb-2">
                    <v-icon>mdi-plus</v-icon>
                    <v-tooltip activator="parent" location="top">zoomIn</v-tooltip>
                </v-btn>
            </div>
        </v-bottom-navigation>
    </v-app>
</template>

<script>

import PdfTitlebar from './PdfTitlebar.vue';
import PdfToc from './PdfToc.vue';

export default {
    name: 'PdfReader',
    components: {
        PdfTitlebar,
        PdfToc
    },
    props: {
        book: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            url: 'https://pdfobject.com/pdf/sample.pdf',
            show: false,
            bookInstance: null,
            rendition: null,
            pdfDoc: null,
            page: 1,
            totalPages: 0,
            toc: [],
            isTocVisible: false,
            manualPage: '',
            scale: 0.5,
            showSnackbar: false,
            snackbarText: '',
            snackbarColor: '',
        };
    },
    watch: {
        page(newVal) {
            this.manualPage = newVal.toString();
            this.updatePlaceholder();
        }
    },
    methods: {
        async loadPdf() {

            try {
                await this.getBook();
                const loadingTask = pdfjsLib.getDocument(this.url);
                this.pdfDoc = await loadingTask.promise;
                this.totalPages = this.pdfDoc.numPages;
                this.loadToc();
                this.renderPage();
                this.updatePlaceholder();
                this.show = true;

            } catch (error) {
                console.error('Error loading PDF Book:', error);
                this.snackbarText = "Error loading the PDF book.";
                this.snackbarColor = 'danger';
                this.showSnackbar = true;
            }
        },
        async getBook() {
            try {
                await frappe.call({
                    method: "library_management.api.api.get_external_book",
                    args: {
                        aws_key: this.book.aws_key,
                    },
                    freeze: true,
                    freeze_message: __("Fetching book details..."),
                    callback: (r) => {
                        if (r.message) {
                            this.url = r.message;
                        }
                    },
                });
            } catch (error) {
                this.snackbarText = "Error loading the book.";
                this.snackbarColor = 'danger';
                this.showSnackbar = true;
            }
        },
        async renderPage() {
            console.log('1111');
            try {
                const page = await this.pdfDoc.getPage(this.page);
                const canvas = document.getElementById('pdf-canvas');
                const context = canvas.getContext('2d');

                const container = canvas.parentElement;
                const containerWidth = container.clientWidth;
                const viewport = page.getViewport({ scale: this.scale });
                const scale = containerWidth / viewport.width;
                const scaledViewport = page.getViewport({ scale: scale });

                canvas.width = scaledViewport.width;
                canvas.height = scaledViewport.height;

                const renderContext = {
                    canvasContext: context,
                    viewport: scaledViewport,
                };
                await page.render(renderContext).promise;

            } catch (error) {
                console.error('Error rendering page:', error);
            }
        },
        async loadToc() {
            const outline = await this.pdfDoc.getOutline();
            if (outline) {
                this.toc = await this.parseOutlineItems(outline);
            }
        },
        async parseOutlineItems(items, result = []) {
            for (const item of items) {
                if (item.dest) {
                    try {
                        let pageNumber = null;
                        if (typeof item.dest === 'string') {
                            const destination = await this.pdfDoc.getDestination(item.dest);
                            if (destination) {
                                if (typeof destination === 'string') {
                                    // Handle named destination
                                    const destRef = await this.pdfDoc.getDestination(destination[0]);
                                    pageNumber = destRef ? await this.pdfDoc.getPageIndex(destRef[0]) + 1 : null;
                                } else if (destination instanceof Array && destination[0]) {
                                    // Handle explicit destination
                                    pageNumber = await this.pdfDoc.getPageIndex(destination[0]) + 1;
                                }
                            }
                        } else if (item.dest instanceof Array && item.dest[0]) {
                            pageNumber = await this.pdfDoc.getPageIndex(item.dest[0]) + 1;

                        }

                        result.push({
                            id: item.dest,
                            title: item.book_title.trim(),
                            pageNumber,
                        });
                    } catch (error) {
                        result.push({
                            id: item.dest,
                            title: item.book_title.trim(),
                            pageNumber: null,
                        });
                    }
                }
                if (item.items.length) {
                    await this.parseOutlineItems(item.items, result);
                }
            }
            return result;
        },
        navigateToPage(pageNum) {
            pageNum = parseInt(pageNum, 10);
            if (pageNum && pageNum >= 1 && pageNum <= this.totalPages) {
                this.page = pageNum;
                this.renderPage();
                this.updatePlaceholder();
            } else {
                this.snackbarText = "The page number is out of bounds.";
                this.snackbarColor = 'info';
                this.showSnackbar = true;
            }
        },
        updatePlaceholder() {
            this.manualPage = `${this.page}/${this.totalPages}`;
        },
        nextPage() {
            if (this.book.digital_file_type === 'pdf' && this.page < this.totalPages) {
                this.page++;
                this.renderPage();
                this.updatePlaceholder();
            }
        },
        previousPage() {
            if (this.book.digital_file_type === 'pdf' && this.page > 1) {
                this.page--;
                this.renderPage();
                this.updatePlaceholder();
            }
        },
        closeReader() {
            if (document.fullscreenElement) {
                document.exitFullscreen();
            }
            this.show = false;
            this.$emit('close-reader');
        },
        toggleToc() {
            this.isTocVisible = !this.isTocVisible;
        },
        zoomIn() {
            const pdfCanvas = document.querySelector('#pdf-canvas');
            pdfCanvas.style.width = `${pdfCanvas.offsetWidth * 1.1}px`;
            pdfCanvas.style.height = `${pdfCanvas.offsetHeight * 1.1}px`;
        },
        zoomOut() {
            const pdfCanvas = document.querySelector('#pdf-canvas');
            pdfCanvas.style.width = `${pdfCanvas.offsetWidth / 1.1}px`;
            pdfCanvas.style.height = `${pdfCanvas.offsetHeight / 1.1}px`;
        }
    },
    created() {
        this.loadPdf();
    },
};
</script>

<style scoped>
.v-card {
    padding: 0 !important;
    margin: 0 !important;
}

.pdf-container {
    overflow-y: auto;
    max-height: 80vh;
    width: 100%;
    display: block;
    justify-content: center;
}

#pdf-canvas {
    width: 700px;
    height: auto;
    display: block;
    margin: 0 auto;
}

.wrap-text {
    white-space: normal;
    word-wrap: break-word;
    width: 100%;
}

.page-input-field .v-field__input {
    width: 40px;
    font-weight: bold;
    color: black;
}
</style>